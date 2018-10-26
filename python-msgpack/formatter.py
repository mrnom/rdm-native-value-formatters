import msgpack

from python_utils.base import BaseFormatter

__version__ = '0.0.1'
DESCRIPTION = 'Python msgpack native formatter'


class MsgpackFormatter(BaseFormatter):
    description = DESCRIPTION
    version = __version__

    def format(self, value):
        try:
            return msgpack.unpackb(value, encoding='utf-8')
        except msgpack.UnpackValueError as e:
            return self.process_error(
                message='Cannot unpack value: {}'.format(e))


if __name__ == "__main__":
    MsgpackFormatter().main()
