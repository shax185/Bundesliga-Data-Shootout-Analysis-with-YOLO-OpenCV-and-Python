from utils import read_video, save_video
from tracker import Tracker 

def main():
    #read video
    video_frames = read_video('input_video/08fd33_4.mp4')
    
    #initialize
    tracker = Tracker('models/best.pt')
    
    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=True,
                                       stub_path='stubs/track_stubs.pkl')

    #save video
    save_video(video_frames, 'output_video/output_video.avi')

if __name__  == '__main__':
    main()