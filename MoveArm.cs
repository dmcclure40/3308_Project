using UnityEngine;
using System.Collections;

public class MoveArm : MonoBehaviour {

    public Rigidbody rb;
    float x = 0.2f;
    // Use this for initialization
    void Start () {
        rb = GetComponent<Rigidbody>();
    }
	
	// Update is called once per frame
	void Update () {
        if (Input.GetKeyUp(KeyCode.UpArrow))
            /// print("the up arrow was pressed");
            MoveArmUp();
       
	}

    void MoveArmUp()
    {
        

    }
}
