using UnityEngine;
using System.Collections;

public class MoveArm : MonoBehaviour {

    public Rigidbody rb;

    float force = 5f;
    float NewForce = 0.85f;
    // Use this for initialization
    void Start () {
        rb = GetComponent<Rigidbody>();
    }
	
	// Update is called once per frame
	void FixedUpdate () {
        if (Input.GetKeyDown(KeyCode.DownArrow))
            MoveArmDown();
        if (Input.GetKeyDown(KeyCode.UpArrow))
            MoveArmUp(); 



    }

    void MoveArmDown()
    {
        print("a key was pressed");
        //NewForce -= force;
        print("force = " + NewForce);
        transform.Rotate(Vector3.forward, -force * Time.deltaTime, Space.Self);

    }

    void MoveArmUp()
    {
        print("a key was pressed");
        //NewForce += force;
        print("force = " + NewForce);
        transform.Rotate(Vector3.forward, force *Time.deltaTime, Space.Self);

    }
}
