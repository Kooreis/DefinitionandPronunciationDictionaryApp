# Python Documentation

# Python Dictionary Script

This Python script provides a simple text-based interface to get the definition and pronunciation of English words. It uses the DictionaryAPI to fetch the data and Google Text-to-Speech (gTTS) to generate the pronunciation.

## Libraries Used

- `json`: This is a standard Python library used for parsing and manipulating JSON data. In this script, it is used to parse the response from the DictionaryAPI which is in JSON format.

- `requests`: This is a popular Python library used for making HTTP requests. It abstracts the complexities of making requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your application.

- `gtts`: The gTTS (Google Text-to-Speech) library is a Python interface for Google's Text-to-Speech API. It allows you to convert text into speech which can be saved as an mp3 file. In this script, it is used to generate the pronunciation of the word.

- `os`: This is a standard Python library used for interacting with the operating system. In this script, it is used to play the generated mp3 file containing the pronunciation of the word.

## How to Use

When you run the script, you will be presented with three options:

1. Get Definition: If you choose this option, you will be asked to enter a word. The script will then fetch and display the definition of the word.

2. Get Pronunciation: If you choose this option, you will be asked to enter a word. The script will then fetch the pronunciation of the word, generate an mp3 file, and play it.

3. Exit: This option will exit the script.

If you enter an invalid choice, the script will display an error message and ask you to choose again.

## Note

This script requires an internet connection to fetch the data from the DictionaryAPI and to generate the pronunciation using gTTS.

---

# C# Documentation

# CSharp Dictionary Script

This script is a simple console application written in C#. It creates a dictionary of words with their definitions and pronunciations, and allows the user to enter a word to retrieve its definition and pronunciation.

## Script Explanation

The script begins by importing two libraries:

- `System`: This is a fundamental library in C# that provides classes for handling standard I/O, string manipulation, threading, and many other functionalities.

- `System.Collections.Generic`: This library provides classes and interfaces that define generic collections, which allow users to create strongly typed collections that provide better type safety and performance than non-generic strongly typed collections.

The script then defines a `Program` class with a `Main` method, which is the entry point for the application.

Inside the `Main` method, a dictionary is created with string keys and Tuple values. Each Tuple contains two strings: the definition and pronunciation of the word. Two entries are added to the dictionary: "apple" and "banana".

The script then enters an infinite loop, where it prompts the user to enter a word. The entered word is converted to lowercase and checked against the keys in the dictionary. If the word is found, its definition and pronunciation are printed to the console. If the word is not found, a message is printed to the console indicating that the word was not found in the dictionary.

## Code Snippet

```CSharp
using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        Dictionary<string, Tuple<string, string>> dictionary = new Dictionary<string, Tuple<string, string>>();
        dictionary.Add("apple", new Tuple<string, string>("A round fruit with red or yellow or green skin", "/ˈæpəl/"));
        dictionary.Add("banana", new Tuple<string, string>("A long curved fruit with yellow skin", "/bəˈnænə/"));

        while (true)
        {
            Console.WriteLine("Enter a word:");
            string word = Console.ReadLine().ToLower();

            if (dictionary.ContainsKey(word))
            {
                Console.WriteLine("Definition: " + dictionary[word].Item1);
                Console.WriteLine("Pronunciation: " + dictionary[word].Item2);
            }
            else
            {
                Console.WriteLine("Word not found in dictionary.");
            }
        }
    }
}
```

This script is a simple yet effective demonstration of how to use dictionaries and Tuples in C#, as well as how to handle user input and output in a console application.

---

# Java Documentation

# Dictionary App

This is a simple Java application that simulates a dictionary. The user can enter a word and the application will return the definition and pronunciation of the word if it exists in the dictionary. The application will continue to prompt the user for words until the user enters 'exit'.

## Code Explanation

The script uses three libraries:

1. `java.util.HashMap`: This library is used to create a HashMap data structure. A HashMap stores key-value pairs. In this application, the key is a word and the value is an array of strings where the first element is the definition of the word and the second element is the pronunciation.

2. `java.util.Map`: This library provides the Map interface which is implemented by the HashMap class. The Map interface includes methods for basic operations (such as put, get, and remove), bulk operations (such as putAll and clear), and collection views (such as keySet, entrySet, and values).

3. `java.util.Scanner`: This library is used to read the user's input. In this application, it is used to read the word that the user enters.

The application starts by creating a HashMap and populating it with some words, their definitions, and pronunciations. Then it enters a loop where it prompts the user to enter a word. If the word is 'exit', it breaks the loop and the application ends. If the word exists in the dictionary, it prints the definition and pronunciation. If the word does not exist in the dictionary, it prints a message saying that the word was not found.

## Usage

To use the application, simply run it and enter a word when prompted. If you want to quit the application, enter 'exit'.

---
