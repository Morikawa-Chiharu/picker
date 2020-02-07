#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file TidyUpManager_idl_examplefile.py
 @brief Python example implementations generated from TidyUpManager.idl
 @date $Date$


"""

import omniORB
from omniORB import CORBA, PortableServer
import ogata, ogata__POA



class TidyUpManager_i (ogata__POA.TidyUpManager):
    """
    @class TidyUpManager_i
    Example class implementing IDL interface ogata.TidyUpManager
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        pass

    # RETURN_VALUE tidyup(in RTC::TimedPose2D path, in RTC::TimedString kind)
    def tidyup(self, path, kind):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result



class StringNavigationCommanderService_i (ogata__POA.StringNavigationCommanderService):
    """
    @class StringNavigationCommanderService_i
    Example class implementing IDL interface ogata.StringNavigationCommanderService
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        pass

    # RETURN_VALUE move(in RTC::TimedPose2D path)
    def move(self, path):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result



class Picker_i (ogata__POA.Picker):
    """
    @class Picker_i
    Example class implementing IDL interface ogata.Picker
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        pass

    # RETURN_VALUE pick(in RTC::TimedString kind)
    def pick(self, kind):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result



class Droper_i (ogata__POA.Droper):
    """
    @class Droper_i
    Example class implementing IDL interface ogata.Droper
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        pass

    # RETURN_VALUE drop(in RTC::TimedString kind)
    def drop(self, kind):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result


if __name__ == "__main__":
    import sys
    
    # Initialise the ORB
    orb = CORBA.ORB_init(sys.argv)
    
    # As an example, we activate an object in the Root POA
    poa = orb.resolve_initial_references("RootPOA")

    # Create an instance of a servant class
    servant = TidyUpManager_i()

    # Activate it in the Root POA
    poa.activate_object(servant)

    # Get the object reference to the object
    objref = servant._this()
    
    # Print a stringified IOR for it
    print orb.object_to_string(objref)

    # Activate the Root POA's manager
    poa._get_the_POAManager().activate()

    # Run the ORB, blocking this thread
    orb.run()

