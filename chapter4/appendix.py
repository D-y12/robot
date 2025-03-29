import numpy as np
import roboticstoolbox as rtb
from abc import ABC, abstractmethod # python mechanisms to create abstract classes
class numercial_IK(ABC):
    """
    An abstract super class which provides basic functionality to perform numerical inverse
    kinematics (IK). Superclasses can inherit this class and implement the solve method.
    This class also provides a mechanism to collect data on performance for large scale
    experiments.
    """
    def __init__(
        self,
        name: str ="IK Solver",
        ilimit: int =30,
        slimit: int =100,
        tol: float =1e-6,
        we: np.ndarray =np.ones(6),
        problems: int =1000,
    ):
        """
        name: The name of the IK algorithm
        ilimit: How many iterations are allowed within a search before a new search is
        started
        slimit: How many searches are allowed before being deemed unsuccessful
        tol: Maximum allowed residual error E
        we: A 6 vector which assigns weights to Cartesian degrees-of-freedom
        problems: Total number of IK problems within the experiment
        """
        # Solver parameters
        self.name =name
        self.slimit =slimit
        self.ilimit =ilimit
        self.tol =tol
        self.We =np.diag(we)
        # Solver results
        self.success =np.zeros(problems)
        self.searches =np.zeros(problems)
        self.iterations =np.zeros(problems)
        # initialise with NaN
        self.searches[:] =np.nan
        self.iterations[:] =np.nan
        self.success[:] =np.nan
    def solve(self, ets: rtb.ETS, Tep: np.ndarray, q0: np.ndarray):
        """
        This method will attempt to solve the IK problem and obtain joint coordinates
        which result the the end-effector pose Tep.
        The method returns a tuple:
        q: The joint coordinates of the solution (ndarray). Note that these will not
        be valid if failed to find a solution
        success: True if a solution was found (boolean)
        iterations: The number of iterations it took to find the solution (int)
        searches: The number of searches it took to find the solution (int)
        residual: The residual error of the solution (float)
        """
        # Iteration count
        i = 0
        total_i =0
        for search in range(self.slimit):
            q = q0[search].copy()
            while i <=self.ilimit:
                i += 1
                # Attempt a step
                # try:
                E, q =self.step(ets, Tep, q)
                # except np.linalg.LinAlgError:
                # i = np.nan
                # break
                # Check if we have arrived
                if E <self.tol:
                    return q, True, total_i +i, search +1, E
            total_i +=i
            i = 0
        # If we make it here, then we have failed
        return q, False, np.nan, np.nan, E
    def error(self, Te: np.ndarray, Tep: np.ndarray):
        """
        Calculates the engle axis error between current end-effector pose Te and
        the desired end-effector pose Tep. Also calulates the quadratic error E
        which is weighted by the diagonal matrix We.
        Returns a tuple:
        e: angle-axis error (ndarray in R^6)
        E: The quadratic error weighted by We
        """
        e = rtb.angle_axis(Te, Tep)
        E = 0.5 *e @ self.We @ e
        return e, E
    @abstractmethod
    def step(self, ets: rtb.ETS, Tep: np.ndarray, q: np.ndarray):
        """
        Superclasses will implement this method to perform a step of the implemented
        IK algorithm
        """
        pass