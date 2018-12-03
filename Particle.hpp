//
//  Particle.hpp
//  Proj2
//
//  Created by Ian Squiers and Erik Wurman on 10/12/18.
//


#ifndef Particle_hpp
#define Particle_hpp

#include <stdio.h>
#include <vector>


// lets be consistent with position and location. easier to read
class Particle {

    private:
        double pbestVal;
        double* pbestLoc; // these are arrays of x_i values representing position or velocity in d dimensions
        double* position;
        double* velocity;
        int dimensions;

    public:
        std::vector <Particle*> neighborhood; // We don;t include this particle in the neighbors

        Particle(int dimensions, double startPosMin, double startPosMax, double startVelMin, double startVelMax);
        Particle(int dimensions, double startPosMin, double startPosMax, double startVelMin, double startVelMax, std::vector<Particle*> neighborhood);

        double getPBestVal() { return this->pbestVal; }
        double* getPBestLoc() { return this->pbestLoc; }
        double* getPosition() { return this->position; }
        double* getVelocity() { return this->velocity; }
        
        void setPBestLoc(double* loc);
        void setPBestVal(double val) { this->pbestVal = val; }

        double* getNBestLoc();
        void update_position();
        void update_velocity();
        void update_velocity2(int iteration); //maybe parameters like inertia rate, etc or make them constants
        void clearNeighborhood();
        void printVelocity();
        Particle getcopy();
};



#endif /* Particle_hpp */
