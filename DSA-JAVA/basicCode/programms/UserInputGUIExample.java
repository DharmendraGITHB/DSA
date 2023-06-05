import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class UserInputGUIExample {
    public static void main(String[] args) {
        // Create a JFrame (window) and set its properties
        JFrame frame = new JFrame("User Input GUI Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);
        frame.setLayout(new GridLayout(3, 2));

        // Create JLabels, JTextFields, and a JButton
        JLabel nameLabel = new JLabel("Enter your name: ");
        JTextField nameField = new JTextField();
        JLabel ageLabel = new JLabel("Enter your age: ");
        JTextField ageField = new JTextField();
        JButton submitButton = new JButton("Submit");

        // Add components to the JFrame
        frame.add(nameLabel);
        frame.add(nameField);
        frame.add(ageLabel);
        frame.add(ageField);
        frame.add(submitButton);

        // Add an ActionListener to the button
        submitButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String name = nameField.getText();
                int age = Integer.parseInt(ageField.getText());
                JOptionPane.showMessageDialog(frame, "Hello, " + name + "! You are " + age + " years old.");
            }
        });

        // Set the JFrame visible
        frame.setVisible(true);
    }
}
