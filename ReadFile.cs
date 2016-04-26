using UnityEngine;
using System.Collections;
using System;
using System.Text;
using System.IO;

public class ReadFile : MonoBehaviour
{


    FileStream fs = new FileStream("input.txt", FileMode.Open, FileAccess.Read, FileShare.ReadWrite);

    StreamReader sr;



    public ReadFile()
    {

        using (StreamReader sr = new StreamReader(fs))
        {

            string line;
            int currentLineNumber = 0;
            decimal xpos = 0;
            //decimal xposnew = 0;
            decimal ypos = 0;
            //decimal yposnew = 0;

            while (!sr.EndOfStream)
            {
                currentLineNumber++;
                line = sr.ReadLine();

                // Debug.Log(line);

                try
                {
                    switch (currentLineNumber)
                    {
                        case 1:
                            xpos = decimal.Parse(line);
                            Debug.Log("xpos = " + xpos);
                            break;
                        case 2:
                            ypos = decimal.Parse(line);
                            Debug.Log("ypos = " + ypos);
                            break;
                    }



                }

                catch (Exception ex)
                {
                    Debug.Log("Error: " + ex.Message + ". Exiting.");
                }

            }

        }

    }
}