# snap-temp-sensor

This is a small Ubuntu Snap to use as a template/demo.

The snap contains a small Python app which simulates a temperature sensor via MQTT. Currently the Snap configuration snap/snapcraft.yaml is prepared for using the Snap on Ubuntu Core (arm64), which can be easily changed into another architecture.

Here you can find more information about creating/building Snaps with Snapcraft: https://snapcraft.io/docs/snapcraft-overview

The snap can be build on a normal Ubuntu distribution. Install snapcraft:

```
$ snap install snapcraft --classic
snapcraft 7.2.9 van Canonical✓ installed
```

Get the Snap Temperature Sensor from the Gitlab repository:

```
$ git@git.etb.tieto.com:ConsumerElectronics/matter.git
$ cd snap-temp-sensor
```

To generate the snap file for `arm64`, execute this command. This will cross-compile the snap for the platform specified in the `snap/snapcraft.yaml`

```
$ snapcraft remote-build
```

Now open a SFTP connection via SSH and copy the `temp-sensor_0.1dev_arm64.snap` file to the Ubuntu Core device.

Open a SSH terminal to the Ubuntu Core device and install the generated Snap file:

```
$ snap install temp-sensor_0.1dev_arm64.snap --devmode
```

This is the command to run the temperature sensor simulation via MQTT (you can press Ctrl-C to stop the simulation):

```
$ temp-sensor
```
