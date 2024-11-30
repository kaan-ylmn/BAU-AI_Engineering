#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <vector>
#include <algorithm>
#include <ctime>
#include <unordered_map>

std::regex fileNames("(GET )(\\w+\\.[a-z]+)");

void addElement(const std::string &filename, std::unordered_map<std::string, int>& dataMap) {
    auto mapIterator = dataMap.find(filename);
    if (mapIterator != dataMap.end()) {
        mapIterator->second++;
    }

    else {
        dataMap.emplace(filename, 1);
    }
}

void mapToVec(const std::unordered_map<std::string, int>& dataMap, std::vector<std::unordered_map<std::string, int>>& vect) {
    vect.reserve(dataMap.size());
    for (const auto& mapped : dataMap) {
        vect.push_back({ {mapped.first, mapped.second} });
    }
}

bool compareMaps(const std::unordered_map<std::string, int>& dataMap1, const std::unordered_map<std::string, int>& dataMap2) {
    return dataMap1.begin()->second > dataMap2.begin()->second;
}

int main() {

    std::unordered_map<std::string, int> mapSearch;

    clock_t start;
    const std::string filePath = ".\\access_log"; //An intermediate variable was used here so that the code can be changed to run with files in different directories easily.
    std::ifstream in_file(filePath);

    if (!in_file) {
        std::cerr << "Problem opening file: " << filePath << "\n";
        return 1;
    }

    std::string line;
    std::smatch matchResult;

    start = clock();

    while (getline(in_file, line)) {
        if (std::regex_search(line, matchResult, fileNames)) {
            addElement(matchResult[2], mapSearch);
        }
    }

    float mapTime = (clock() - start) / static_cast<float>CLOCKS_PER_SEC;

    std::vector<std::unordered_map<std::string, int>> vect;
    mapToVec(mapSearch, vect);

    std::sort(vect.begin(), vect.end(), compareMaps);

    float sortTime = ((std::clock() - start) / static_cast<float>CLOCKS_PER_SEC) - mapTime;

    for (int i = 0; i < 10; ++i) {
        for (auto entry = vect[i].begin(); entry != vect[i].end(); ++entry) {
            std::cout << entry->first << ": " << entry->second << "\n";
        }
    }

    float duration = (std::clock() - start) / static_cast<float>CLOCKS_PER_SEC;

    std::cout << "\nTime for mapping: " << mapTime << " seconds\n";
    std::cout << "Time for sorting: " << sortTime << " seconds\n";
    std::cout << "\nTOTAL TIME: " << duration << " seconds\n";

    in_file.close();
    return 0;
}