//
//  utils.cpp
//  Fireworks
//
//  Created by Ian Squiers on 12/10/18.
//  Copyright © 2018 Ian Squiers. All rights reserved.
//

#include "utils.hpp"
#include <math.h>


vector<double> random_vect(int size, double low_bound, double upper_bound) {
    vector<double> vect;
    for (int i = 0; i < size; i++) {
        vect.push_back(randomDoubleInRange(low_bound, upper_bound));
    }
    return vect;
}

vector<double> subtract_vect(vector<double> &v1, vector<double> &v2) {
    vector<double> return_vect;
    for (int i = 0; i < v1.size(); i++) {
        return_vect.push_back(v1[i] - v2[i]);
    }
    return return_vect;
}

vector<double> add_vect(vector<double> &v1, vector<double> &v2) {
    vector<double> return_vect;
    for (int i = 0; i < v1.size(); i++) {
        return_vect.push_back(v1[i] + v2[i]);
    }
    return return_vect;
}

vector<double> scalar_mult(vector<double> &v1, double scalar) {
    vector<double> return_vect;
    for (int i = 0; i < v1.size(); i++) {
        return_vect.push_back(v1[i] * scalar);
    }
    return return_vect;
}


void getPosRangeForFunction(Function f, double &min, double &max){
    if (f == Rosenbrock){
        min = RosenbrockPosMin;
        max = RosenbrockPosMax;
        return;
    }
    if (f == Ackley){
        min = AckleyPosMin;
        max = AckleyPosMax;
        return;
    }
    if (f == Rastrigin){
        min = RastriginPosMin;
        max = RastriginPosMax;
        return;
    }
}

void getVelRangeForFunction(Function f, double &min, double &max){
    if (f == Rosenbrock){
        min = RosenbrockVelMin;
        max = RosenbrockVelMax;
        return;
    }
    if (f == Ackley){
        min = AckleyVelMin;
        max = AckleyVelMax;
        return;
    }
    if (f == Rastrigin){
        min = RastriginVelMin;
        max = RastriginVelMax;
        return;
    }
}

double randomDoubleInRange(double fMin, double fMax)
{
    double f = (double)rand() / RAND_MAX;
    return fMin + f * (fMax - fMin);
}

double evaluateRosenbrock(double* pos, int dimensions){
    double total = 0;
    for (int i = 0; i < dimensions - 1; i++){
        total += 100*(pos[i+1] - pos[i]*pos[i])*(pos[i+1] - pos[i]*pos[i]) + (pos[i] - 1)*(pos[i] - 1);
    }
    return total;
}

double evaluateAckley(double* pos, int dimensions){
    double firstSum = 0, secondSum = 0.0;
    for (int i =0; i < dimensions; i++){
        firstSum += pos[i]*pos[i];
        secondSum += cos(2 * M_PI * pos[i]);
    }
    return -20.0 * exp(-0.2*sqrt(firstSum / (double)dimensions)) - exp(secondSum / (double) dimensions) + 20 + M_E;
}

double evaluateRastrigin(double* pos, int dimensions){
    double fitness = 10 * dimensions;
    for (int i = 0; i < dimensions; i++){
        fitness += pos[i]*pos[i] - (10 * cos(2 * M_PI * pos[i]));
    }
    return fitness;
}
