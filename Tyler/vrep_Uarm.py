import vrep

class VrepUArm:
  def __init__(self):
    vrep.simxFinish(-1) # just in case, close all opened connections
    self.clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)



    res, self.leftJointDynamic  = vrep.simxGetObjectHandle(self.clientID, "DynamicLeftJoint",  vrep.simx_opmode_oneshot_wait)
    res, self.rightJointDynamic = vrep.simxGetObjectHandle(self.clientID, "DynamicRightJoint", vrep.simx_opmode_oneshot_wait)


  def to_direction(self, direction):
    direction_vector = self.direction_v[direction]
    self.linearVelocityLeft  += direction_vector[0]
    self.linearVelocityRight += direction_vector[1]
    self.set_motors()

  # private
  def set_motors(self):
    t_left  = self.linearVelocityLeft  / self.wheelRadius
    t_right = self.linearVelocityRight / self.wheelRadius
    vrep.simxSetJointTargetVelocity(self.clientID, self.leftJointDynamic,  t_left,  vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetVelocity(self.clientID, self.rightJointDynamic, t_right, vrep.simx_opmode_oneshot_wait)
