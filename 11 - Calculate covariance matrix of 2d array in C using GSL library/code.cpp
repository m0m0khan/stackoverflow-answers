/*  
First, you have to put this data in a file, say test.dat, then you can read it in a gsl_matrix and calculate the covariance matrix using the gsl_stats_covariance function as follows:
*/

#include <stdio.h>
#include <gsl/gsl_statistics.h>
#include <gsl/gsl_matrix.h>

int main (void)
{
  int i, j;
  int rows = 55, col = 2;
  
  gsl_matrix * m = gsl_matrix_alloc (rows, col);
  gsl_matrix * C = gsl_matrix_alloc (col, col);
  
  {
     FILE * f = fopen ("test.dat", "rb");
     gsl_matrix_fscanf (f, m);
     fclose (f);
  }
  
  for (i = 0; i < m->size2; i++) 
  {
        for (j = 0; j < m->size2; j++) 
        {
          gsl_vector_view col1, col2;  
          col1 = gsl_matrix_column (m, i);
          col2 = gsl_matrix_column (m, j);
          double cov = gsl_stats_covariance(col1.vector.data, col1.vector.stride, 
                                            col2.vector.data, col2.vector.stride, 
                                            col1.vector.size);
          gsl_matrix_set (C, i, j, cov);
        }
    }
    
  for (i = 0; i < C->size1; i++) 
  {
      for (j = 0; j < C->size2; j++) 
        {
            printf("%f ", gsl_matrix_get(C, i, j));
        }
  }

  gsl_matrix_free (m);
  gsl_matrix_free (C);
  
  return 0;
}

/* You can see that the C matrix has been initialized as a 2x2 matrix because the covariance matrix is a square matrix. Each column of the matrix m is sliced as gsl_vector_view and utilized in the gsl_stats_covariance function. In the end, the covariance matrix is printed.
*/
