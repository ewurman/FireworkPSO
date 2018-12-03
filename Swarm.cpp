//
//  Swarm.cpp
//  Proj2
//
//  Created by Ian Squiers and Erik Wurman on 10/12/18.
//

#include "Swarm.hpp"
#include "Particle.cpp"
#include <vector>
#include <cfloat>
#include <iostream>

Swarm::Swarm(int iterations, int numParticles, int dimensions, Function f, NeighborhoodTopology topology){
    this->numIterations = iterations;
    this->swarmSize = numParticles;
    this->dimensions = dimensions;
    this->function = f;
    this->topology = topology;
    this->globalBestLoc = new double[dimensions];
    this->globalBestVal = DBL_MAX;
    double minPos, maxPos, minVel, maxVel;
    getPosRangeForFunction(f, minPos, maxPos);
    getVelRangeForFunction(f, minVel, maxVel);
    for (int i = 0; i < numParticles; i++){
        Particle p = *new Particle(dimensions, minPos, maxPos, minVel, maxVel);
        this->particles.push_back(p);
    }
    initializeNeighborhoods();
}

void Swarm::initializeNeighborhoods(){
    if (this->topology == Global){
        global(this->particles);
    }
    if (this->topology == Ring){
        ring(this->particles);
    }
    if (this->topology == VonNeumann){
        vonNeumann(this->particles);
    }
    if (this->topology == Random){
        randNeighbors(this->particles, randomNeighborNum);
    }
}


void Swarm::updateThenEvaluate() {
	for (int i = 0; i < this->swarmSize; i++) {
        this->particles[i].printVelocity();
        this->particles[i].update_position();
        this->particles[i].update_velocity();
        double eval;
        double* location = this->particles[i].getPosition();
        switch (this->function) {
            case Rosenbrock:
                eval = evaluateRosenbrock(location, this->dimensions);
                break;
            case Ackley:
                eval = evaluateAckley(location, this->dimensions);
                break;
            case Rastrigin:
                eval = evaluateRastrigin(location, this->dimensions);
            default:
                break;
        }
        if (eval < this->particles[i].getPBestVal()) {
            this->particles[i].setPBestLoc(location);
            this->particles[i].setPBestVal(eval);
        }
        if (eval < this->globalBestVal){
            for (int j = 0; j < this->dimensions; j++){
                this->globalBestLoc[j] = location[j];
            }
            this->globalBestVal = eval;
        }
	}
}

void Swarm::updateThenEvaluate2(int iteration) {
    for (int i = 0; i < this->swarmSize; i++) {
        //this->particles[i].printVelocity();
        this->particles[i].update_position();
        this->particles[i].update_velocity2(iteration);
        double eval;
        double* location = this->particles[i].getPosition();
        switch (this->function) {
            case Rosenbrock:
                eval = evaluateRosenbrock(location, this->dimensions);
                break;
            case Ackley:
                eval = evaluateAckley(location, this->dimensions);
                break;
            case Rastrigin:
                eval = evaluateRastrigin(location, this->dimensions);
            default:
                break;
        }
        if (eval < this->particles[i].getPBestVal()) {
            this->particles[i].setPBestLoc(location);
            this->particles[i].setPBestVal(eval);
        }
        if (eval < this->globalBestVal){
            for (int j = 0; j < this->dimensions; j++){
                this->globalBestLoc[j] = location[j];
            }
            this->globalBestVal = eval;
        }
    }
}

void Swarm::evaluate() {
    for (int i = 0; i < this->swarmSize; i++) {
        double eval;
        double* location = this->particles[i].getPosition();
        switch (this->function) {
            case Rosenbrock:
                eval = evaluateRosenbrock(location, this->dimensions);
                break;
            case Ackley:
                eval = evaluateAckley(location, this->dimensions);
                break;
            case Rastrigin:
                eval = evaluateRastrigin(location, this->dimensions);
            default:
                break;
        }
        if (eval < this->particles[i].getPBestVal()) {
            this->particles[i].setPBestLoc(location);
            this->particles[i].setPBestVal(eval);
        }
        if (eval < this->globalBestVal){
            for (int j = 0; j < this->dimensions; j++){
                this->globalBestLoc[j] = location[j];
            }
            this->globalBestVal = eval;
        }
    }
}

void Swarm::rerandomizeNeighborhoods(){
    for (int i = 0; i < this->swarmSize; i++){
        particles[i].clearNeighborhood();
    }
    randNeighbors(this->particles, randomNeighborNum);
}


void Swarm::pso(){
    //evaluate(); // we want an initial location for pbest and pbestval
	for (int i = 0; i < this->numIterations; i++) {
        updateThenEvaluate2(i);
        //cout << "Best value so far found of " << this->globalBestVal << endl;
	}
    cout << "Best value found of " << this->globalBestVal << endl;
}

double Swarm::pso2(){
    //evaluate(); // we want an initial location for pbest and pbestval
    for (int i = 0; i < this->numIterations; i++) {
        updateThenEvaluate2(i);
        if (this->topology == Random){
            //20% chance to change the neighborhoods
            double chance = (double) rand() / RAND_MAX;
            if (chance < rerandomizeChance){
               rerandomizeNeighborhoods();
            }
        }
        //cout << "Best value so far found of " << this->globalBestVal << endl;
    }
    //cout << "Best value found of " << this->globalBestVal << endl;
    return this->globalBestVal;
}


