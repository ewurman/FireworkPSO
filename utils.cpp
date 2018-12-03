// Utilities file for PSO code
//
//


#ifndef UTILS_CPP
#define UTILS_CPP

#include "Particle.hpp"
#include "utils.hpp"
#include <vector>
#include <math.h>


using namespace std;

/*
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
*/

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


int** vnArray(int rows, int columns) {
    int ** indecies = new int*[rows];
    int count = 0;
    for (int i = 0; i < rows; i++) {
        indecies[i] = new int[columns];
        for (int j = 0; j < columns; j++) {
            indecies[i][j] = count;
            count++;
        }
    }
    return indecies;
}


void vonNeumann(std::vector<Particle> &particles) {
	int rows = 0;
	switch (particles.size()) {
		case 16 : rows = 4; break;
		case 30 : rows = 5; break;
		case 49 : rows = 7; break;
	}
	int columns = particles.size()/rows;
	int ** vn = vnArray(rows, columns);
	int rup, rdown, cr, cl;

	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < rows; j++) {
			rup = i - 1;
			rdown = i + 1;
			cl = j - 1;
			cr = j + 1;

			if (i == 0) {
				rup = rows - 1;
				rdown = i + 1;
			}
			if (i == (rows-1)) {
				rup = i - 1;
				rdown = 0;
			}
			if (j == 0){
				cl = columns - 1;
				cr = j + 1;
			}
			if (j == columns - 1) {
				cl = j - 1;
                cr = 0;
			}
			particles[vn[i][j]].neighborhood.push_back(&particles[vn[rup][j]]); // up
			particles[vn[i][j]].neighborhood.push_back(&particles[vn[rdown][j]]); // down
			particles[vn[i][j]].neighborhood.push_back(&particles[vn[i][cr]]); // right
			particles[vn[i][j]].neighborhood.push_back(&particles[vn[i][cl]]); // left
		}
	}
}

void ring(vector<Particle> &particles) {
	for (int i = 0; i < particles.size(); i++) {
		if (i == 0){
			particles[i].neighborhood.push_back(&particles[particles.size()-1]);
			particles[i].neighborhood.push_back(&particles[i+1]);
		}
		else if (i == (particles.size() - 1)){
			particles[i].neighborhood.push_back(&particles[i-1]);
			particles[i].neighborhood.push_back(&particles[0]);
		}
		else {
			particles[i].neighborhood.push_back(&particles[i+1]);
			particles[i].neighborhood.push_back(&particles[i-1]);
		}
	}
}


void global(vector<Particle> &particles) {
	for (int i = 0; i < particles.size(); i++) {
		for (int j = 0; j < particles.size(); j++) {
			if (i != j) {
				particles[i].neighborhood.push_back(&particles[j]);
			}
		}
	}
}


void randNeighbors(vector<Particle> &particles, int numNeighbors) {
	vector<Particle*> copy;
	for (int i = 0; i < particles.size(); i++) {
		copy.push_back(&particles[i]);
	}
	for (int i = 0; i < particles.size(); i++) {
		random_shuffle ( copy.begin(), copy.end());
		for (int j = 0; j < numNeighbors; j++) {

			particles[i].neighborhood.push_back(copy[j]);
			
		}
	}
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

/*
double evaluateRastrigin(double* pos, int dimensions){ //sphere
	double total = 0;
	for (int i = 0; i < dimensions; i++){
		total += pos[i] * pos[i];
	}
    return total;
}
*/


#endif
