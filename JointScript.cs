using UnityEngine;
using System.Collections;

public class JointScript : MonoBehaviour
{

    public Rigidbody rb;
    public float RotateSpeed = 50f;
    // Use this for initialization
    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        if (Input.GetKeyDown(KeyCode.LeftArrow))
        {
            MoveJointLeft();
        }
        if (Input.GetKeyDown(KeyCode.RightArrow))
        {
            MoveJointRight();
        }
    }

    void MoveJointLeft()
    {
        transform.Rotate(-RotateSpeed * Time.deltaTime, 0f, 0f);
    }

    void MoveJointRight()
    {
        transform.Rotate(RotateSpeed * Time.deltaTime, 0f, 0f);
    }
}
