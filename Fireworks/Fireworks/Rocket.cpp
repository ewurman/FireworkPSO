//
//  Rocket.cpp
//  Fireworks
//
//  Created by Ian Squiers on 12/9/18.
//  Copyright © 2018 Ian Squiers. All rights reserved.
//

#include "Rocket.hpp"
#include "utils.hpp"

Rocket::Rocket(vector<double> origin, vector<double> velocity) {
    this->origin = origin;
    this->location = origin;
    this->pbest = origin;
    this->velocity = velocity;
}

void Rocket::launch(int num_steps) {
    double best = this->evaluate();
    for (int i = 0; i < num_steps; i++) {
        this->location = add_vect(this->location, this->velocity);
        if (this->evaluate() > best) {
            
        }
    }
}
