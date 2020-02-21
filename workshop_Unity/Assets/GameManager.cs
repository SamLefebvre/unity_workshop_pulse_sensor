using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameManager : MonoBehaviour
{
    GameObject cube;
    float timeA;
    float timeB;
    // Start is called before the first frame update
    void Start()
    {
        cube = GameObject.Find("Cube");
        timeA = Time.time;
        timeB = Time.time;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.B))
        {
            cube.GetComponent<Rigidbody>().AddForce(3 * Vector3.up, ForceMode.Impulse);
            timeA = Time.time;
            Debug.Log(timeA - timeB);
            if ((timeA - timeB) < 5) // Press under 5 seconds
            {
                Debug.Log("OK");
            }

        }
        if (Input.GetKeyDown(KeyCode.N))
        {
            cube.GetComponent<Rigidbody>().AddForce(5 * Vector3.up, ForceMode.Impulse);
            timeB = Time.time;
        }
    }
}
