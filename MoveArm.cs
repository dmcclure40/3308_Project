using UnityEngine;
using System.Collections;
using System.IO;

public class MoveArm : MonoBehaviour {

    public Rigidbody rb;
    public float RotateSpeed = 50f;
    public TextAsset textFile;
    public float Y = 300f;
    public float tempY = 100;

    // Use this for initialization
    void Start () {
        rb = GetComponent<Rigidbody>();
        //string text = textFile.text;
    }
	
	// Update is called once per frame
	void FixedUpdate () {
        //print(textFile);
         if (Y > tempY)
        {
            print(Y);
            print(tempY);
            MoveArmDown();
            Y = tempY;
            print(Y);
        }
        if(Y < tempY)
        {
            MoveArmUp();
            Y = tempY;
        }
    }

    void MoveArmDown()
    {
        transform.Rotate(0f, 0f, RotateSpeed * Time.deltaTime);
    }

    void MoveArmUp()
    {
        transform.Rotate(0f, 0f, -RotateSpeed * Time.deltaTime);
    }
}
