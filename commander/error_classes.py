import commander.ErrorCodes as ErrorCodes
import logging
import traceback

logger = logging.getLogger('docker.error_classes')


class SabError(Exception):
    def __init__(self, msg, error_code, interface_err=None):
        self.msg = msg
        self.error_code = error_code
        self.interface_err = interface_err
        # log debug message that contains traceback
        log_message = 'Input Parameters: message="%s" error_code="%i" Interface_error="%s"\n' % \
                      (self.msg, self.error_code, interface_err)
        for item in traceback.format_stack():
            log_message += item
        # logger.debug(log_message) TODO: Enable this after fixing all log types

        super(SabError, self).__init__(msg)


class SysCommandError(SabError):
    def __init__(self, return_code, cout, cerr, command):
        cout = cout.decode('utf-8')
        cerr = cerr.decode('utf-8')
        self.msg = "System command '%s' returned error code: '%s'\ncout: '%s'\ncerr: '%s'" % (
            command, return_code, cout, cerr)
        self.error_code = ErrorCodes.STUB_ERROR
        self.return_code = return_code
        self.cout = cout
        self.cerr = cerr
        self.interface_err = 'Error in system command (return code is not 0)'
        self.command = command
        super(SabError, self).__init__(self.msg)


class SysCommandTimeout(SabError):
    def __init__(self, command, timeout):
        self.msg = "Command '%s' timed out after %s seconds" % (command, timeout)
        self.error_code = ErrorCodes.STUB_TIMEOUT_ERROR
        self.interface_err = 'SysCommandTimeout'
        self.command = command
        super(SabError, self).__init__(self.msg)
