#! /bin/bash

decomposePar

# Change deltaT (and related control parameters)
#sed -i -e 's/endTime 0.001/endTime 1.5/g' ./system/controlDict

# Run for remaining time with larger deltaT
mpirun -x LD_LIBRARY_PATH -x PATH -x WM_PROJECT_DIR \
   -x WM_PROJECT_INST_DIR -x WM_OPTIONS -x FOAM_LIBBIN \
   -x FOAM_APPBIN -x MPI_BUFFER_SIZE \
   -np 20 foamRun -parallel > log &