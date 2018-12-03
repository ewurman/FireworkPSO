//
//  utils.h
//  Proj2
//
//  Created by Ian Squiers on 10/16/18.
//  Copyright © 2018 Ian Squiers. All rights reserved.
//

#ifndef utils_hpp
#define utils_hpp

#include <stdio.h>
#include <vector>
#include "Particle.hpp"

using namespace std;

enum Function {
    Rosenbrock,
    Ackley,
    Rastrigin
};

enum NeighborhoodTopology {
    Global,
    Ring,
    VonNeumann,
    Random
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

int** vnArray(int rows, int columns);


void vonNeumann(vector<Particle> &particles);


void global(vector<Particle> &particles);

void ring(vector<Particle> &particles);


void randNeighbors(vector<Particle> &particles, int numNeighbors);


double evaluateRosenbrock(double* pos, int dimensions);

double evaluateAckley(double* pos, int dimensions);

double evaluateRastrigin(double* pos, int dimensions);

#endif /* utils_h */
