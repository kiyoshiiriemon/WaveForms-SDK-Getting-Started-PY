from WF_SDK import device, scope, wavegen, tools, error   # import instruments

import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
times = []
ch1 = []
ch2 = []

time0 = time.time()

def animate(i, times, ch1, ch2):
    v1 = scope.measure(device_data, channel=1)
    v2 = scope.measure(device_data, channel=2)

    times.append(time.time() - time0)
    ch1.append(v1)
    ch2.append(v2)

    times = times[-100:]
    ch1 = ch1[-100:]
    ch2 = ch2[-100:]

    ax.clear()
    ax.plot(times, ch1)
    ax.plot(times, ch2)

    plt.title('Voltage (last 100 measurements)')
    plt.ylabel('Voltage')
    plt.xlabel('Time (sec)')

device_data = device.open()
ani = animation.FuncAnimation(fig, animate, fargs=(times, ch1, ch2), interval=0)
plt.show()
device.close(device_data)

