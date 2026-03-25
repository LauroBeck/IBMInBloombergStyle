#include <iostream>
#include <iomanip>
#include <string>

int main(int argc, char* argv[]) {
    std::string ticker = (argc > 1) ? argv[1] : "IBM";
    std::cout << "\033[1;37;44m " << ticker << " US Equity             1) News  2) Charts  3) Financials \033[0m" << std::endl;
    std::cout << std::endl;
    std::cout << "\033[1;33m--- BLOOMBERG REAL-TIME [BDP] ---\033[0m" << std::endl;
    std::cout << std::left << std::setw(12) << "SECURITY" << std::setw(12) << "LAST" << "CHANGE" << std::endl;
    std::cout << std::left << std::setw(12) << ticker << std::setw(12) << "240.59" << "\033[31m-7.80 (-3.14%)\033[0m" << std::endl;
    return 0;
}
