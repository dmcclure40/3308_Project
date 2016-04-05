using UnityEngine;
using System.Collections;

public class GripperLeft : MonoBehaviour
{
    public Rigidbody rb;
    float gripperStatus = 0f; //open
    Vector3 GR;
    // Use this for initialization
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        GR = transform.position;
    }


    void Update()
    {
        if (Input.GetKeyUp(KeyCode.Space))
        {
            if (gripperStatus == 0f)
            {
                closeGripper();
                print("gripper status is closed and spacebar is pressed");
            }

            else {
                openGripper();
                print("gripper status is open and spacebar is pressed");
            }
        }
    }

    void closeGripper()
    {
        GR.z += 0.059f;
        transform.position = GR;
        gripperStatus = 1f;
        print("Gripper status is" + gripperStatus);
    }

    void openGripper()
    {
        GR.z -= 0.059f;
        transform.position = GR;
        gripperStatus = 0f;
        print("Gripper status is" + gripperStatus);
    }
}