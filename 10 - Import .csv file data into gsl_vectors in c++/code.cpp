 #include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <gsl/gsl_vector.h>

int main ()
{
  int i = 0, rows = 7;

  // Allocate vectors
  gsl_vector *X = gsl_vector_alloc (rows);
  gsl_vector *Y = gsl_vector_alloc (rows);
  gsl_vector *Z = gsl_vector_alloc (rows);
  
  // Open the file
  std::ifstream openfile("data.csv");
  openfile.ignore(10000,'\n'); // Ignore the header
  std::string line;
  
  while (getline(openfile, line, '\n'))
  {
    std::string a, b, c;
    std::stringstream iss(line);
    getline(getline(getline (iss, a, ','), b, ','), c, ',');
    // std::cout << a << ' ' << b << ' ' << c << std::endl;
    
    // Set vectors
    gsl_vector_set (X, i, std::stod(a));
    gsl_vector_set (Y, i, std::stod(b));
    gsl_vector_set (Z, i, std::stod(c));
    
    i += 1;
  }
  
  // Close the file
  openfile.close();
    
  for(i = 0; i < rows; ++i)
  {
      // Get vectors
      std::cout << gsl_vector_get (X, i) << "\t";
      std::cout << gsl_vector_get (Y, i) << "\t";
      std::cout << gsl_vector_get (Z, i) << "\n";
  }
  
  // Do some processing with the vectors

  // Free allocated memory at the end
  gsl_vector_free (X);
  gsl_vector_free (Y);
  gsl_vector_free (Z);

  return 0;
}
