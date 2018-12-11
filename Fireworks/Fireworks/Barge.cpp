//
//  Barge.cpp
//  Fireworks
//
//  Created by Ian Squiers on 12/9/18.
//  Copyright © 2018 Ian Squiers. All rights reserved.
//

// Barges are where fireworks are shot from

#include "Barge.hpp"
#include "Rocket.hpp"
#include "utils.hpp"

// rotating rockets
void rotating(int dimensions, int num_rockets, int num_iterations) {
    vector<Rocket> rockets;
    vector<double> origin = random_vect(dimensions, 0.0, 1.0);
    for (int i = 0; i<num_rockets; i++) {
        vector<double> velocity = random_vect(dimensions, 0.0, 1.0);
        rockets.push_back(Rocket(origin, velocity)); // each has same vector but random velocity
    }
    for(int i = 0; i < num_iterations; i++) {
        
        // GET EVALUATIONS ALONG VELOCITY PATH
        for (int i = 0; i < num_rockets; i++) {
            rockets[i].launch(10); // define num of evaluations
        }
        
        // **** ADD LOCAL SEARCH HERE****
        
        // SET ORIGIN TO PBEST AND DIRECTION
        for (int i = 0; i < num_rockets; i++) {
            if (i + 1 != num_rockets) {
                rockets[i].origin = rockets[i].pbest;
                vector<double> direction = subtract_vect(rockets[i+1].pbest, rockets[i].origin);
                rockets[i].velocity = scalar_mult(direction, 0.1); // how much do we reduce the velocity by
            }
            else {
                rockets[i].origin = rockets[i].pbest;
                vector<double> direction = subtract_vect(rockets[0].pbest, rockets[i].origin);
                rockets[i].velocity = scalar_mult(direction, 0.1); // how much do we reduce the velocity by
            }
        }
    }
}
