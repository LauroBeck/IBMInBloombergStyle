#include <iostream>
#include <iomanip>
#include <string>

void print_des(std::string ticker) {
    std::cout << "\033[1;37;44m " << ticker << " US Equity             Security Description (DES) \033[0m" << std::endl;
    std::cout << std::endl;
    std::cout << "\033[1;33mCOMPANY PROFILE\033[0m" << std::endl;
    std::cout << "Name:       International Business Machines Corp" << std::endl;
    std::cout << "Sector:     Technology" << std::endl;
    std::cout << "Industry:   IT Services & Consulting" << std::endl;
    std::cout << "Market Cap: ~220B USD" << std::endl;
    std::cout << std::endl;
    std::cout << "\033[1;33mBUSINESS SUMMARY\033[0m" << std::endl;
    std::cout << "IBM provides integrated solutions and services worldwide. It operates" << std::endl;
    std::cout << "through Software, Consulting, Infrastructure, and Financing segments," << std::endl;
    std::cout << "with a heavy focus on Hybrid Cloud and AI (Watsonx)." << std::endl;
    std::cout << std::endl;
    std::cout << "\033[1;34m------------------------------------------------------------\033[0m" << std::endl;
}

int main(int argc, char* argv[]) {
    std::string ticker = (argc > 1) ? argv[1] : "IBM";
    print_des(ticker);
    return 0;
}
