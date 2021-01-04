//Name: Adam Petty
//File: freq.cpp
//Performs frequency analysis on a given txt file

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>


bool second_sort(std::pair<std::string, int>&, std::pair<std::string, int>&);
void analysis(std::string*);

int main(int argc, char ** argv)
{
    std::string book;
	
    std::ifstream file (argv[1]);
    std::getline(file, book);
    file.close();
    
    std::cout << "file : " << argv[1] << std::endl;
    std::cout << "length: " << book.length() << std::endl;
    std::cout << "string: " << book.substr(0, 60) << " ..." << std::endl;
    std::cout << '\n';
    
    analysis(&book);
	 
	 return 0; 
}


void analysis(std::string * book)
{

	std::vector< std::pair <std::string, int>> vect_g1;
	std::vector< std::pair <std::string, int>> vect_g2;
	std::vector< std::pair <std::string, int>> vect_g3;
	std::vector< std::pair <std::string, int>> vect_g4;
	
	std::string g1 = "a";
	std::string g2 = "ab";
	std::string g3 = "abc";
	std::string g4 = "abcd";
    
    int g1_total = 0;
    int g2_total = 0;
    int g3_total = 0;
    int g4_total = 0;

	std::unordered_map<std::string, int> grams = {};
	

	for (int i = 0; i < book->length(); i++)
	{
		g1 = (*book)[i];	
		std::unordered_map<std::string, int>::const_iterator key = grams.find(g1);
		if(key == grams.end())
		{
			grams.emplace(g1, 1);
            g1_total++;
		}
		else
		{
			grams[g1] += 1;
            g1_total++;
		}

		if ((i + 1) < book->length())
		{
			g2 = book->substr(i, 2);
			std::unordered_map<std::string, int>::const_iterator key = grams.find(g2);
			if(key == grams.end())
			{
				grams.emplace(g2, 1);
                g2_total++;
			}
			else
			{
				grams[g2] += 1;
                g2_total++;
			}
		}
		if ((i + 2) < book->length())
		{
			g3 = book->substr(i, 3);
			std::unordered_map<std::string, int>::const_iterator key = grams.find(g3);
			if(key == grams.end())
			{
				grams.emplace(g3, 1);
                g3_total++;
			}
			else
			{
				grams[g3] += 1;
                g3_total++;
			}
		}
		if ((i + 3) < book->length())
		{
			g4 = book->substr(i, 4);
			std::unordered_map<std::string, int>::const_iterator key = grams.find(g4);
			if(key == grams.end())
			{
				grams.emplace(g4, 1);
                g4_total++;
			}
			else
			{
				grams[g4] += 1;
                g4_total++;
			}
		}

	}
    
    //iterates the map and moves data to vector
	for(const auto& x : grams)
	{
					
		std::pair<std::string, int> freq;
		freq.first = x.first;
		freq.second = x.second;
		switch(freq.first.length())
		{
			case 1:
			{
				vect_g1.push_back(freq);
				break;
			}
			case 2:
			{
				vect_g2.push_back(freq);
				break;
			}
			case 3:
			{
				vect_g3.push_back(freq);
				break;
			}
			case 4:
			{
				vect_g4.push_back(freq);
				break;
			}
		}
	}
	
	std::sort(vect_g1.begin(), vect_g1.end(), second_sort);
	std::sort(vect_g2.begin(), vect_g2.end(), second_sort);
	std::sort(vect_g3.begin(), vect_g3.end(), second_sort);
	std::sort(vect_g4.begin(), vect_g4.end(), second_sort);

	//writes the n-grams to the file

	for (int j = 0; j < 26; j++)
	{
		std::cout << vect_g1[j].first << ": " << vect_g1[j].second << ", " << 
                    (double) vect_g1[j].second / (double) g1_total << std::endl;
	} 
		
	for (int j = 0; j < vect_g2.size(); j++)
	{
		std::cout << vect_g2[j].first << ": " << vect_g2[j].second << ", " << 
                    (double) vect_g2[j].second / (double) g2_total << std::endl;
    }
	for (int j = 0; j < vect_g3.size(); j++)
	{
		if (j == 1000) break;
		std::cout << vect_g3[j].first << ": " << vect_g3[j].second << ", " << 
                    (double) vect_g3[j].second / (double) g3_total << std::endl;
	}
	for (int j = 0; j < vect_g4.size(); j++)
	{
		if (j == 1000) break;
		std::cout << vect_g4[j].first << ": " << vect_g4[j].second << ", " << 
                    (double) vect_g4[j].second / (double) g4_total << std::endl;
	}
} 


bool second_sort(std::pair<std::string, int> &a,
				std::pair<std::string, int> &b)
{
	return (a.second > b.second);
}






