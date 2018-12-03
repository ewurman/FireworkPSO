//
//  Particle.cpp
//  Proj2
//
//  Created by Ian Squiers and Erik Wurman on 10/12/18.
//

#include "Particle.hpp"
#include "utils.hpp"
#include <vector>
#include <cfloat>
#include <math.h>

double CONSTRICTION_FACTOR = 0.7298;
double TOWARD_PBEST = 2.05;
double TOWARD_NBEST = 2.05;

Particle::Particle(int dimensions, double startPosMin, double startPosMax, double startVelMin, double startVelMax){
    this->pbestVal = DBL_MAX;
    this->pbestLoc = new double[dimensions];
    this->position = new double[dimensions];
    this->velocity = new double[dimensions];
    for (int i = 0; i < dimensions; i++){
        position[i] = randomDoubleInRange(startPosMin, startPosMax);
        velocity[i] = randomDoubleInRange(startVelMin, startVelMax);
    }
    this->dimensions = dimensions;
    this->neighborhood = *new std::vector<Particle*>();
}
        

Particle::Particle(int dimensions, double startPosMin, double startPosMax, double startVelMin, double startVelMax, std::vector<Particle*> neighborhood){
    this->pbestVal = DBL_MAX;
    this->pbestLoc = new double[dimensions];
    this->position = new double[dimensions];
    this->velocity = new double[dimensions];
    for (int i = 0; i < dimensions; i++){
        position[i] = randomDoubleInRange(startPosMin, startPosMax);
        velocity[i] = randomDoubleInRange(startVelMin, startVelMax);
    }
    this->dimensions = dimensions;
    this->neighborhood = neighborhood;
}


double* Particle::getNBestLoc(){
    double* nbestLoc = this->pbestLoc;
    double nbestVal = this->pbestVal;
    for (int i = 0; i < this->neighborhood.size(); i++){
        double val = this->neighborhood[i]->getPBestVal();
        if (val < nbestVal){
            nbestVal = val;
            nbestLoc = this->neighborhood[i]->getPBestLoc();
        }
    }
    return nbestLoc;
}

void Particle::update_position(){
    for (int i = 0; i < this->dimensions; i++){
        this->position[i] = this->position[i] + this->velocity[i];
    }
}

void Particle::setPBestLoc(double* loc) { 
    for (int i = 0; i < this->dimensions; i++){
        this->pbestLoc[i] = loc[i];
    }

}



void Particle::update_velocity(){
    double* newVelocity = new double[this->dimensions];
    double* nbestLoc = this->getNBestLoc();
    for (int i = 0; i < this->dimensions; i++){
        double random1 = randomDoubleInRange(0, TOWARD_PBEST);
        double random2 = randomDoubleInRange(0, TOWARD_NBEST);
        newVelocity[i] = CONSTRICTION_FACTOR * (this->velocity[i] + random1*(this->pbestLoc[i] - this->position[i]) +
                                                    random2*(nbestLoc[i] - this->position[i]));
    }
    double* toDelete = this->velocity;
    this->velocity = newVelocity;
    delete(toDelete);
}


void Particle::update_velocity2(int iteration){
    if (iteration == 0){ //dont update if we haven't evaluated yet #scaryUninitializedValues
        return;
    }
    double* newVelocity = new double[this->dimensions];
    double* nbestLoc = this->getNBestLoc();
    for (int i = 0; i < this->dimensions; i++){
        double random1 = randomDoubleInRange(0, TOWARD_PBEST);
        double random2 = randomDoubleInRange(0, TOWARD_NBEST);
        newVelocity[i] = CONSTRICTION_FACTOR * (this->velocity[i] + random1*(this->pbestLoc[i] - this->position[i]) +
                                                    random2*(nbestLoc[i] - this->position[i]));
    }
    double* toDelete = this->velocity;
    this->velocity = newVelocity;
    delete(toDelete);
}

void Particle::clearNeighborhood(){
    neighborhood.clear();
}


void Particle::printVelocity(){
    cout << "\t Velocity for particle ";
    double total = 0;
    for (int i = 0; i < this->dimensions; i++){
        cout << velocity[i] << " ";
        total += velocity[i]*velocity[i];
    }
    cout << "  has a magnitude of " << sqrt(total) << endl;
}



