using UnityEngine;
using System.Collections;

public class JointScript : MonoBehaviour
{

    public Rigidbody rb;

    float force = 0.05f;
    float NewForce = 0.9f;
    // Use this for initialization
    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        if (Input.GetKeyDown(KeyCode.DownArrow))
            MoveJointDown();
        if (Input.GetKeyDown(KeyCode.UpArrow))
            MoveJointUp();



    }

    void MoveJointDown()
    {
        print("a key was pressed");
        NewForce -= force;
        print("force = " + NewForce);
        transform.position = new Vector3(transform.position.x, NewForce, transform.position.z);

    }

    void MoveJointUp()
    {
        print("a key was pressed");
        NewForce += force;
        print("force = " + NewForce);
        transform.position = new Vector3(transform.position.x, NewForce, transform.position.z);

    }
}
