/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Copyright (C) 2011-2024 OpenFOAM Foundation
     \\/     M anipulation  |
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version. For more details see: 
    http://www.gnu.org/licenses/

Related
    This boundary condition is derived from turbulentInlet [1]. As 'Tessellate 
    Data Science' we have made minor modifications that we believe aren't 
    enough to constitute a legally-valid 'derivative work' thus OpenFOAM 
    retains copyright.
    [1] https://cpp.openfoam.org/v12/turbulentInletFvPatchField_8H.html

\*---------------------------------------------------------------------------*/

#include "mouthInletVel.H"
#include "addToRunTimeSelectionTable.H"

// * * * * * * * * * * * * * * * * Constructors  * * * * * * * * * * * * * * //

Foam::mouthInletVelFvPatchVectorField::
mouthInletVelFvPatchVectorField
(
    const fvPatch& p,
    const DimensionedField<vector, volMesh>& iF,
    const dictionary& dict
)
:
    fixedValueFvPatchField<vector>(p, iF, dict, false),
    //ranGen_(label(0)),
    ranNormal_(label(0)),
    fluctuationScale_(dict.lookup<scalar>("fluctuationScale", unitFraction)),
    meanAxialVelocity_(dict.lookup<scalar>("meanAxialVelocity", dimVelocity)),
    diffRandVelAcrossCases_(dict.lookup<scalar>("diffRandVelAcrossCases", unitFraction))
{}


Foam::mouthInletVelFvPatchVectorField::
mouthInletVelFvPatchVectorField
(
    const mouthInletVelFvPatchVectorField& ptf,
    const fvPatch& p,
    const DimensionedField<vector, volMesh>& iF,
    const fieldMapper& mapper
)
:
    fixedValueFvPatchField<vector>(ptf, p, iF, mapper),
    //ranGen_(label(0)),
    ranNormal_(label(0)),
    fluctuationScale_(ptf.fluctuationScale_),
    meanAxialVelocity_(ptf.meanAxialVelocity_),
    diffRandVelAcrossCases_(ptf.diffRandVelAcrossCases_)
{}


Foam::mouthInletVelFvPatchVectorField::
mouthInletVelFvPatchVectorField
(
    const mouthInletVelFvPatchVectorField& ptf,
    const DimensionedField<vector, volMesh>& iF
)
:
    fixedValueFvPatchField<vector>(ptf, iF),
    //ranGen_(ptf.ranGen_),
    ranNormal_(ptf.ranNormal_),
    fluctuationScale_(ptf.fluctuationScale_),
    meanAxialVelocity_(ptf.meanAxialVelocity_),
    diffRandVelAcrossCases_(ptf.diffRandVelAcrossCases_)
{}

// * * * * * * * * * * * * * * * Member Functions  * * * * * * * * * * * * * //

// Calculations
void Foam::mouthInletVelFvPatchVectorField::updateCoeffs()
{
    if (this->updated())
    {
        return;
    }

    // access case data
    vectorField& patchField = *this;
    scalarField randomField(this->size());
    scalar t = this->db().time().value();

    // seed according to diffRandVelAcrossCases value
    int seed;
    if ((int) diffRandVelAcrossCases_ == 1) {
        seed = time(NULL); // ~ 1.7e+09 [s]
    } else {
        seed = 1000000000;
    }
    int t_seed = int (t * 1e6);

    // random velocity magnitudes in vertical/horizontal directions
    Random ranNorm1 = Random(seed + t_seed / 1);
    scalar randNormVal1 = ranNorm1.scalarNormal();
    Random ranNorm2 = Random(seed + t_seed / 2);
    scalar randNormVal2 = ranNorm2.scalarNormal();
    Random ranNorm3 = Random(seed + t_seed / 3);
    scalar randNormVal3 = ranNorm3.scalarNormal();

    double randVal1_db = randNormVal1;
    double U_x =  randVal1_db * fluctuationScale_;
    double randVal2_db = randNormVal2;
    double U_z =  randVal2_db * fluctuationScale_;
    double randVal3_db = randNormVal3;
    double turbAxial =  randVal3_db * fluctuationScale_ * 0.2;

    //Info << "# Info: " << randNormVal1 << ", " << randNormVal2 << ", " << randNormVal3 << "\n";

    // update boundary with velocities
    forAll(patchField, facei)
    {
        patchField[facei].component(vector::Y) = meanAxialVelocity_ + turbAxial;
        patchField[facei].component(vector::X) = U_x;
        patchField[facei].component(vector::Z) = U_z;
    }

    //fixedValueFvPatchVectorField::updateCoeffs();
}

// Writing
void Foam::mouthInletVelFvPatchVectorField::write(Ostream& os) const
{
    fvPatchVectorField::write(os);
    writeEntry(os, "fluctuationScale", fluctuationScale_);
    writeEntry(os, "meanAxialVelocity", meanAxialVelocity_);
    writeEntry(os, "diffRandVelAcrossCases", diffRandVelAcrossCases_);
    writeEntry(os, "value", *this);
}


namespace Foam
{
   makePatchTypeField
   (
       fvPatchVectorField,
       mouthInletVelFvPatchVectorField
   );
}

// ************************************************************************* //