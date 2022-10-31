import pathlib


def gen_path(path):
    sub_path = []
    video_path = []
    paths = pathlib.Path(path).iterdir()
    for _ in paths:
        if str(_).split('.')[-1] in ['ass', 'srt']:
            sub_path.append(_)
        if str(_).split('.')[-1] in ['mkv', 'mp4']:
            video_path.append(_)
    sub_path.sort()
    video_path.sort()
    return sub_path, video_path


if __name__ == '__main__':
    v, s = gen_path(r'Z:\video2\link\tv\Pantheon.S01.1080p.AMZN.WEB-DL.DD+5.1.H.264-NTb')

    print(v)
    print(s)
