object = 'locator1'
s_pos = [0.0, 5.0, 7.0] #cmds.xform(object,translation=True, query=True)
e_pos = [20.0, 10.0, 0.0] #cmds.xform(object,translation=True, query=True)

g = -9.8
start_frame = 1
end_frame = 120
key_step = 10
frame_length = end_frame - start_frame
fps = 24.0
time = frame_length/fps
initial_height = s_pos[1]
final_height = e_pos[1]
vi = ((final_height - initial_height) - ((g * t**2)/2))/t
x_inc = (e_pos[0]-s_pos[0])/frame_length
z_inc = (e_pos[2]-s_pos[2])/frame_length

frame_deltas = range(0, frame_length , key_step)
if frame_length not in frame_deltas:
    frame_deltas.append(frame_length)
    
for frame_delta in frame_deltas:
    time_delta = frame_delta/fps
    disp_y = ((g * time_delta**2)/2 + (vi*time_delta)) + initial_height
    print disp_y
    cmds.currentTime(start_frame+frame_delta, update=False)
    #translation = cmds.xform(object,translation=True, query=True)
    translation[0] = s_pos[0] + (x_inc * frame_delta)
    translation[1] = disp_y
    translation[2] = s_pos[2] + (z_inc * frame_delta)
    cmds.setAttr(
    	object + '.translate',
    	translation[0],
    	translation[1],
    	translation[2]
    )
    for attribute in ['tx', 'ty', 'tz']:
        cmds.setKeyframe(
    		object,
    		attribute=attribute,
    	)
