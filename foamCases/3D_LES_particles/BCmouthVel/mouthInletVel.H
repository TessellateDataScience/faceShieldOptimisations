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

Description
    This boundary condition adds significant non-axial velocity magnitude at 
    each timestep (to represent random flow direction during speech), in 
    addition to smaller randomness to represent turbulence. This randomness is 
    non-uniform (a Normal Distribution) within a case run. Note this randomness 
    isn't unique (using identical parameter values) across cases.

Usage
    Syntax for applying this boundary condition:

    <patchName>
    {
        type                    mouthInletVel;
        fluctuationScale        1.0;
        meanAxialVelocity       0.5;
        diffRandVelAcrossCases  1;
    }

    fluctuationScale  
        Distribution factor (of mean flow magnitude) in non-axial directions:
         - Normal distribution defaults to range:[-4, 4] with a stdDev:[-1, 1].
    diffRandVelAcrossCases
        Randomises the velocity fluctuations across differing cases (simulations)
        - 1 = yes, 0 = no

Customisation
    Developing custom boundary conditions: 
     | - https://www.tfd.chalmers.se/~hani/kurser/OS_CFD_2022/lectureNotes/implementParabolicVelocityFixedValueBoundaryCondition.pdf
    
    Software development process:
     |--Design: Conceptualise using 'pseudocode: 
     |   - Interpretation of algorithm in form of annotations & informative text 
     |     (in natural language):
     |       www.geeksforgeeks.org/how-to-write-a-pseudo-code
     |--Coding: Developing then removing compiler errors:
     |    https://en.wikipedia.org/wiki/Debugging#Techniques
     |--Testing: Part of'verification' in computational-science land:
     |   - 'Unit testing' to ensure expected behaviour.

\*---------------------------------------------------------------------------*/

#ifndef mouthInletVelFvPatchVectorField_H
#define mouthInletVelFvPatchVectorField_H

#include "randomGenerator.H"
#include "Random.C"
#include "fixedValueFvPatchFields.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

/*---------------------------------------------------------------------------*\
                 Class mouthInletVelFvPatchVectorField Declaration
\*---------------------------------------------------------------------------*/

class mouthInletVelFvPatchVectorField
:
    public fixedValueFvPatchVectorField
{
    // Private Data

        //- Random number generator
        //randomGenerator ranGen_;
        Random ranNormal_;

        //- Fluctuation scale
        scalar fluctuationScale_;

        //- Reference field
        scalar meanAxialVelocity_;

        //- Randomise velocity across cases
        scalar diffRandVelAcrossCases_;

        //- Current time index (used for updating)
        label curTimeIndex_;


public:

    //- Runtime type information
    TypeName("mouthInletVel");


    // Constructors

        //- Construct from patch, internal field and dictionary
        mouthInletVelFvPatchVectorField
        (
            const fvPatch&,
            const DimensionedField<vector, volMesh>&,
            const dictionary&
        );

        //- Construct by mapping given mouthInletVelFvPatchVectorField
        //  onto a new patch
        mouthInletVelFvPatchVectorField
        (
            const mouthInletVelFvPatchVectorField&,
            const fvPatch&,
            const DimensionedField<vector, volMesh>&,
            const fieldMapper&
        );

        //- Disallow copy without setting internal field reference
        mouthInletVelFvPatchVectorField
        (
            const mouthInletVelFvPatchVectorField&
        ) = delete;

        //- Copy constructor setting internal field reference
        mouthInletVelFvPatchVectorField
        (
            const mouthInletVelFvPatchVectorField&,
            const DimensionedField<vector, volMesh>&
        );

        //- Construct and return a clone setting internal field reference
        virtual tmp<fvPatchVectorField> clone
        (
            const DimensionedField<vector, volMesh>& iF
        ) const
        {
            return tmp<fvPatchVectorField>
            (
                new mouthInletVelFvPatchVectorField(*this, iF)
            );
        }


    // Member Functions

        // Access

            //- Return the fluctuation scale
            const scalar& fluctuationScale() const
            {
                return fluctuationScale_;
            }

            //- Return reference to the fluctuation scale to allow adjustment
            scalar& fluctuationScale()
            {
                return fluctuationScale_;
            }

            //- Return the reference field
            const scalar& meanAxialVelocity() const
            {
                return meanAxialVelocity_;
            }

            //- Return reference to the reference field to allow adjustment
            scalar& meanAxialVelocity()
            {
                return meanAxialVelocity_;
            }

            //- Return the randomising switch
            const scalar& diffRandVelAcrossCases() const
            {
                return diffRandVelAcrossCases_;
            }

            //- Return reference to the reference field to allow adjustment
            scalar& diffRandVelAcrossCases()
            {
                return diffRandVelAcrossCases_;
            }


        //- Update the coefficients associated with the patch field
        virtual void updateCoeffs();

        //- Write
        virtual void write(Ostream&) const;
};


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

#endif

// ************************************************************************* //