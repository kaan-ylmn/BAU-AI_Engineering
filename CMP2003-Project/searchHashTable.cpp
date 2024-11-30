#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <vector>
#include <algorithm>
#include <ctime>

std::regex fileAmount("\\d+");
std::regex fileNames("(GET )(\\w+\\.[a-z]+)");

class Node {
//A Node class that is used in storing filenames and their number of total visits while we add them to the hash table.
public:
    int value;
    std::string documentName;

    Node(int value = 0, std::string documentName = "")
        : value(value), documentName(documentName) {}
};

class HashTable {
//The main data structre which is used to store filenames and their total values.
private:
    static const int SIZE = 16384; //A power of 2 is used to make the hashing process faster.
    std::vector<std::vector<Node>> dataTable;

public:
    HashTable() {
        for (int i{ 0 }; i < SIZE; i++)
            dataTable.push_back({});
    }

    int hashFunc(std::string key) {
        std::smatch matchResult;
        if (std::regex_search(key, matchResult, fileAmount))
            return std::stoi(matchResult[0]) % SIZE;
        return 0;
    }

    void addElement(const std::string& documentName) {
        int index = hashFunc(documentName);
        bool found = false;

        for (auto& element : dataTable[index]) {
            if (element.documentName == documentName) {
                element.value++;
                found = true;
                break;
            }
        }

        if (!found) {
            Node newNode(1, documentName);
            dataTable[index].emplace_back(newNode);
        }
    }

//We enter the sorting methods after this point, heap sort was used because of it's speed and efficiency.

    void heapify(std::vector<Node>& currentBucket, int heapSize, int i) {
        int smallest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        if (left < heapSize && currentBucket[left].value < currentBucket[smallest].value)
            smallest = left;
        if (right < heapSize && currentBucket[right].value < currentBucket[smallest].value)
            smallest = right;
        if (smallest != i) {
            std::swap(currentBucket[i], currentBucket[smallest]);
            heapify(currentBucket, heapSize, smallest);
        }
    }

    void heapSort(std::vector<Node>& currentBucket, int heapSize) {
        for (int i = heapSize / 2 - 1; i >= 0; i--)
            heapify(currentBucket, heapSize, i);

        for (int i = heapSize - 1; i >= 0; i--) {
            std::swap(currentBucket[0], currentBucket[i]);
            heapify(currentBucket, i, 0);
        }
    }

    void sort() {
        int length = dataTable.size();
        std::vector<Node> nodes;
        int i = 0;
        int j = 0;

        while (i != length) {
            int currentSize = dataTable[i].size() - 1;
            if (j <= currentSize) {
                auto& currentElement = dataTable[i][j];
                nodes.push_back(currentElement);
                j++;
            }
            else {
                j = 0;
                i++;
            }
        }

        heapSort(nodes, nodes.size());

        int count = 0;
        for (auto entry : nodes) {
            if (count < 10)
                std::cout << entry.documentName << ": " << entry.value << "\n";
            count++;
        }
    }
};

int main() {

    std::clock_t start;
    const std::string filePath = ".\\access_log"; //An intermediate variable was used here so that the code can be changed to run with files in different directories easily.
    std::ifstream in_file(filePath);

    if (!in_file) {
        std::cerr << "Problem opening file: " << filePath << "\n";
        return 1;
    }

    std::string line;
    std::smatch matchResult;
    HashTable hashSearch;
    start = std::clock();

    while (std::getline(in_file, line)) {
        if (std::regex_search(line, matchResult, fileNames)) {
            hashSearch.addElement(matchResult[2]);
        }
    }

    float hashTime = (std::clock() - start) / static_cast<float>CLOCKS_PER_SEC;

    hashSearch.sort();
    float sortTime = ((std::clock() - start) / static_cast<float>CLOCKS_PER_SEC) - hashTime;


    float duration = (std::clock() - start) / static_cast<float>CLOCKS_PER_SEC;

    std::cout << "\nTime for hashing: " << hashTime << " seconds\n";
    std::cout << "Time for sorting: " << sortTime << " seconds\n";
    std::cout << "\nTOTAL TIME: " << duration << " seconds\n";

    in_file.close();
    return 0;
}
