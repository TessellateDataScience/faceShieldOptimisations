#! /bin/bash

mpirun -x LD_LIBRARY_PATH -x PATH -x WM_PROJECT_DIR \
   -x WM_PROJECT_INST_DIR -x WM_OPTIONS -x FOAM_LIBBIN \
   -x FOAM_APPBIN -x MPI_BUFFER_SIZE \
   -np 20 foamRun -parallel > log &