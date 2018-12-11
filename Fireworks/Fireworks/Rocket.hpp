//
//  Rocket.hpp
//  Fireworks
//
//  Created by Ian Squiers on 12/9/18.
//  Copyright © 2018 Ian Squiers. All rights reserved.
//

#ifndef Rocket_hpp
#define Rocket_hpp

#include <stdio.h>
#include <vector>
#include "Barge.hpp"

using namespace std;

class Rocket : public Barge {
public:
    Rocket(vector<double> origin, vector<double> velocity);
    void launch(int num_steps);
    vector<double> origin;
    vector<double> velocity;
    vector<double> pbest;
private:
    vector<double> location;
    double evaluate();
};

#endif /* Rocket_hpp */
