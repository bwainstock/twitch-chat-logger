import argparse
from manager import TwitchManager
from utils import parse_channels_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--streams-to-log", dest="channels_amount", type=int,
                        help="the number of streams to log", default=100)
    parser.add_argument("-f", "--log-filename", dest="log_filename",
                        help="the filename to log to", default=None)
    parser.add_argument("-c", "--channels", dest="channels", type=str, nargs='+',
                        help="the specific channel names to log", default=[])
    parser.add_argument("-l", "--channel-list", dest="channels_list", type=str, nargs='?',
                        help="the filename with a list of channels", default=None)
    args = parser.parse_args()

    if args.channels_list:
        real_channels = parse_channels_list(args.channels_list)
    else:
        real_channels = args.channels

    manager = TwitchManager(channels_amount=args.channels_amount,
                            channels=real_channels,
                            log_filename=args.log_filename)

    try:
        manager.run_log_loop()
    except KeyboardInterrupt:
        print 'Exiting gracefully...'
        manager.stop_bot()

if __name__ == "__main__":
    main()
