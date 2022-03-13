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