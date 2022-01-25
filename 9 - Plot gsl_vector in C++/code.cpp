/* 
After some research, I got to know that it is not directly possible to plot gsl_vector in C++. However, I coded a workaround (almost like the one suggested by bitmask) using gnuplot, which solved my problem. Therefore, I am posting an answer to my own question.

Following is my solution:
*/ 


#include <stdio.h>
#include <gsl/gsl_vector.h>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>

void plot(const gsl_vector *x, const gsl_vector *y);

using namespace std;

int main ()
{
  int i;
  gsl_vector * x = gsl_vector_alloc (10);
  gsl_vector * y = gsl_vector_alloc (10);

  for (i = 0; i < 10; i++)
    {
      gsl_vector_set (x, i, i);
      gsl_vector_set (y, i, exp(i));
    }
  
  plot(x, y);

  gsl_vector_free (x);
  gsl_vector_free (y);
  return 0;
}

void plot(const gsl_vector *x, const gsl_vector *y)
{
  string command_filename = "commands.txt";
  ofstream command;
  string data_filename = "data.txt";
  ofstream data;
  int j;
  string plot_filename = "plot.png";

  cout << "\n";
  cout << "plot:\n";
  cout << "  Write command and data files that can be used\n";
  cout << "  by gnuplot for a plot.\n";

//  Create the data file.

  data.open ( data_filename.c_str ( ) );

  for ( j = 0; j < x->size; j++ )
  {
    data << "  " << gsl_vector_get(x, j)
         << "  " << gsl_vector_get(y, j) << "\n";
  }

  data.close ( );

  cout << "\n";
  cout << "  plot: data stored in '"
       << data_filename << "'\n";
       
//  Create the command file.

  command.open ( command_filename.c_str ( ) );

  command << "# " << command_filename << "\n";
  command << "#\n";
  command << "# Usage:\n";
  command << "#  gnuplot < " << command_filename << "\n";
  command << "#\n";
  command << "set term png\n";
  command << "set output '" << plot_filename << "'\n";
  command << "set xlabel 'X'\n";
  command << "set ylabel 'Y'\n";
  command << "set title 'Plot using gnuplot'\n";
  command << "set grid\n";
  command << "set style data lines\n";
  command << "plot '" << data_filename << "' using 1:2 with lines\n";
  command << "quit\n";

  command.close ( );

  cout << "  plot: plot commands stored in '"
       << command_filename << "'\n";

  return;
}

/*
In main(), I generated two gsl vectors and then passed them to the plot function. In the plot function, I write these vectors to a file called data.txt. I then generate a command file commands.txt which can then be read by gnuplot using the data.txt file.

After running the code above, I manually write the following command:

gnuplot < commands.txt

in terminal/console to plot the vectors which yields the plot.
*/
