#include <iostream>
#include <iomanip>
#include <random>
#include <string>
struct Telemetry{std::string deviceId;double fillPercent,temperatureC,batteryPercent;};
Telemetry readSensors(){static std::mt19937 rng{42};std::uniform_real_distribution<double> fill(55,98),temp(26,34),battery(60,100);return {"SW-204",fill(rng),temp(rng),battery(rng)};}
int main(){std::cout<<"EcoGrid C++ Smart Bin Telemetry Simulator\n";for(int i=0;i<5;i++){auto t=readSensors();std::cout<<std::fixed<<std::setprecision(1)<<"{\"device_id\":\"" <<t.deviceId<<"\",\"fill_percent\":"<<t.fillPercent<<",\"temperature_c\":"<<t.temperatureC<<",\"battery_percent\":"<<t.batteryPercent<<"}\n";}return 0;}