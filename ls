#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <chrono>
#include <thread>

// Bloomberg-style Data Structure
struct Security {
    std::string ticker;
    double price;
    double change;
    std::string sector;
};

void display_row(const Security& s) {
    std::string color = (s.change >= 0) ? "\033[32m" : "\033[31m"; // Green/Red
    std::cout << std::left << std::setw(10) << s.ticker 
              << std::setw(12) << s.price 
              << color << std::setw(10) << (s.change >= 0 ? "+" : "") << s.change << "%" << "\033[0m"
              << std::setw(15) << s.sector << std::endl;
}

int main(int argc, char* argv[]) {
    // Simulated Bloomberg Data Cache
    std::map<std::string, Security> market = {
        {"GM", {34.52, 1.25, "Consumer"}},
        {"PETR4", {38.10, -0.45, "Energy"}},
        {"TSLA", {175.22, 2.10, "Auto"}}
    };

    if (argc < 2) {
        std::cout << "Usage: ./bloomberg_bin [TICKER]" << std::endl;
        return 1;
    }

    std::string query = argv[1];
    if (market.count(query)) {
        std::cout << "\033[1;33m--- BLOOMBERG REAL-TIME (BDP) ---\033[0m" << std::endl;
        display_row(market[query]);
    } else {
        std::cout << "Ticker " << query << " not found in local cache." << std::endl;
    }

    return 0;
}
