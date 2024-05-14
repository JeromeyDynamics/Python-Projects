package frc.robot;

public class Constants {
    public static final class DriveConstants {
        //move motors
        public static final int kRightFrontMotorID = 1;
        public static final int kLeftFrontMotorID = 2;
        public static final int kRightRearMotorID = 3;
        public static final int kLeftRearMotorID = 4;
        //encoders for movement
        public static final int kLeftEncoderlA = 0;
        public static final int kLeftEncoderlB = 1;
        public static final int kRightEncoderlA = 2;
        public static final int kRightEncoderlB = 3;

        public static final double kEncoderTick2Meter = 1.0 / 4096.0 * 0.128 * Math.PI;
        public static final double kAutoDriveForwardSpeed = 0.5;
        public static final double kAutoDriveForwardDistance = 1.5;
    
        public static final Double kTurnFunctionValue = 1.5;
        public static final Double kSpeedFunctionValue = 1.5;
    }
    public static final class ShooterConstants {
        //shooter
        public static final int kShooter1 = 2;
        public static final int kShooter2 = 3;
        
        public static final int kMotorPort = 2;
        public static final int kShooterEncoderlA = 4;
        public static final int kShooterEncoderlB = 5;
        public static final double kEncoderTick2Meter = 1.0 / 4096.0 * 0.1 * Math.PI;
        public static final double kP = 3;
        public static final double kI = 0;
        public static final double kD = 0.8;

        public static final double kRaisedPosition = 1.2;
        public static final double kLoweredPosition = 0;
        public static final double kJoystickMaxSpeed = 0.5;
    }
    public static final class IntakeConstants {
        public static final int kLeftMotorPort = 3;
        public static final int kRightMotorPort = 4;
        public static final double kOpenSpeed = -1;
        public static final double kClosedSpeed = 1;
        public static final int kIntakeEncoderlA = 6;
        public static final int kIntakeEncoderlB = 7;
        public static final double kEncoderTick2Meter = 1.0 / 4096.0 * 0.1 * Math.PI;
    }
    public static final class OIConstants {
        //joystick
        public static final int kJoystickPort = 0;
        //set default command
        public static final int kArcadeDriveSpeedAxis = 1;
        public static final int kArcadeDriveTurnAxis = 3;
        //button commands
        public static final int kShooterOuttakeButton = 3;
        public static final int kShooterInttakeButton = 4;
        public static final int kIntakeCloseButtonIdx = 5;
    }
}
