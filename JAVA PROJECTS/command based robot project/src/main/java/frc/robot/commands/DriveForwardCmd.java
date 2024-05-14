package frc.robot.commands;

import edu.wpi.first.wpilibj2.command.Command;
import frc.robot.subsystems.DriveSubsystem;

public class DriveForwardCmd extends Command {
    private final DriveSubsystem driveSubsystem;
    private final double distance;
    private double encoderSetpoint;
    
    public DriveForwardCmd(DriveSubsystem driveSubsystem2, double distance) {
        this.driveSubsystem = driveSubsystem2;
        this.distance = distance;
        addRequirements(driveSubsystem2);
    }

    @Override
    public void initialize() {
        encoderSetpoint = driveSubsystem.getEncoderMeters() + distance;
    }

    @Override
    public void execute() {
        DriveSubsystem.setMotors(0.5, 0.5);
    }

    @Override
    public void end(boolean interrupted) {
        DriveSubsystem.setMotors(0, 0);
        System.out.println("DriveForwardCmd ended!");
    }

    @Override
    public boolean isFinished() {
        if (driveSubsystem.getEncoderMeters() > encoderSetpoint)
            return true;
        else
            return false;
    }
}
