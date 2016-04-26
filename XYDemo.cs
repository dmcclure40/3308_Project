using UnityEngine;

public class XYDemo : MonoBehaviour
{
    // Change input.x and input.y in inspector
    // Observe output.x and output.y in inspector
    //public Vector2 input;
    public Vector2 output;
    public TextAsset textFile;

   // XYStreamWriter writer = XYStreamWriter.FromFile("data.txt");
    XYStreamReader reader = XYStreamReader.FromFile("input.txt");

    void Start()
    {
        // Intentionally not reading/writing to disk
        // too often because I care about my hard drive.
        //InvokeRepeating("Write", 0.5f, 1.0f);
        InvokeRepeating("Read", 1.0f, 1.0f);
    }

    void OnDestroy()
    {
        //writer.Dispose();
        reader.Dispose();
    }

    void Read()
    {
        print("Read...");
        reader.Read();
        print(output);
        output = reader.XY;
    }

    //void Write()
    //{
       //print("Write...");
       //writer.XY = input;
       //writer.Write();
   // }
}