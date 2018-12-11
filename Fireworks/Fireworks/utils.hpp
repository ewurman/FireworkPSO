//
//  utils.hpp
//  Fireworks
//
//  Created by Ian Squiers on 12/10/18.
//  Copyright © 2018 Ian Squiers. All rights reserved.
//

#ifndef utils_hpp
#define utils_hpp

#include <stdio.h>
#include <vector>
using namespace std;


vector<double> random_vect(int size, double low_bound, double upper_bound);
vector<double> subtract_vect(vector<double> &v1, vector<double> &v2);
vector<double> add_vect(vector<double> &v1, vector<double> &v2);
vector<double> scalar_mult(vector<double> &v1, double scalar);


////// COPIED with neighborhoods removed

enum Function {
    Rosenbrock,
    Ackley,
    Rastrigin
};

const double RosenbrockPosMin = 15.0;
const double RosenbrockPosMax = 30.0;
const double AckleyPosMin = 16.0;
const double AckleyPosMax = 32.0;
const double RastriginPosMin = 2.56;
const double RastriginPosMax = 5.12;
const double RosenbrockVelMin = -2.0;
const double RosenbrockVelMax = 2.0;
const double AckleyVelMin = -2.0;
const double AckleyVelMax = 4.0;
const double RastriginVelMin = -2.0;
const double RastriginVelMax = 4.0;


void getPosRangeForFunction(Function f, double &min, double &max);

void getVelRangeForFunction(Function f, double &min, double &max);

double randomDoubleInRange(double fMin, double fMax);

double evaluateRosenbrock(double* pos, int dimensions);

double evaluateAckley(double* pos, int dimensions);

double evaluateRastrigin(double* pos, int dimensions);




#endif /* utils_hpp */
