using UnityEngine;
using System.Collections;

public class MoveArm : MonoBehaviour {

    public Rigidbody rb;
    public float RotateSpeed = 50f;
    
    // Use this for initialization
    void Start () {
        rb = GetComponent<Rigidbody>();
    }
	
	// Update is called once per frame
	void FixedUpdate () {
        if (Input.GetKeyDown(KeyCode.DownArrow))
        {
            MoveArmDown();
        }
        if (Input.GetKeyDown(KeyCode.UpArrow))
        {
            MoveArmUp();
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
