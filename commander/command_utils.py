import copy
import hashlib
import sys
import time
import random
import subprocess32

from commander.error_classes import SysCommandError, SysCommandTimeout

def call_stub(cmd, by_shell=False, ignore_return_code=False, cwd=None, timeout=180, no_log=False):
    """ Executes a shell command
    Args:
        cmd (str): Shell command
        by_shell (bool): True if command should be executed using shell
        ignore_return_code (bool): True if no exception should be raised in case of non-zero error code
        cwd (str): Working directory to run command
        timeout(int or None): time in second to wait for command to return return_code
        no_log(bool): disable auto logging
    Returns:
        helper.StubOutput: An object of helper.StubOutput
    """
    
    return_code = -1
    cout = cerr = ""
    try:
        if not by_shell:

            array_command = cmd.split()
            proc = subprocess32.Popen(array_command, stdout=subprocess32.PIPE,
                                      stderr=subprocess32.PIPE, cwd=cwd)
        else:

            proc = subprocess32.Popen(cmd, shell=True, stdout=subprocess32.PIPE,
                                      stderr=subprocess32.PIPE, executable='/bin/bash', cwd=cwd)
        cout, cerr = proc.communicate(timeout=timeout)
        return_code = proc.returncode

        if ignore_return_code is False and return_code != 0:
            raise SysCommandError(return_code, cout, cerr, cmd)
    except subprocess32.TimeoutExpired:
        raise SysCommandTimeout(cmd, timeout)
    except BaseException as e:
        if not isinstance(e, SystemExit):
            raise SysCommandError(return_code, cout, cerr, cmd)
        else:
            raise e
    return cout, cerr, return_code
