# Keylogger 

During my time at Fullstack Academy, we developed a Python-based keylogger program for the Linux operating system as part of a group project.

The name of our program is Keymaster, which records every keystroke until the program is stopped. This program could be modified to be malicious; for example, we could have it forward all keystrokes to an email address, or we could have it run each time the computer reboots.

The aim of the project was to increase awareness of the potential harm caused by phishing emails and educate users on the best practices for verifying the trustworthiness of email attachments and links.

## What exactly is a keylogger?
A keylogger, sometimes called a keystroke logger or keyboard capture, is a type of surveillance technology used to monitor and record each keystroke on a specific device. 

The use of keyloggers dates back to the 1970s, when the Soviet Union developed a hardware keylogging device for electric typewriters. The keylogger, called the Selectric bug, tracked the movements of the printhead by measuring the magnetic field emitted by the movements of the printhead. The Selectric bug targeted IBM Selectric typewriters and spied on U.S. diplomats in the U.S. embassy and consulate buildings in Moscow and St. Petersburg. Selectric keyloggers were found in 16 typewriters and were in use until 1984, when a U.S. ally who was a separate target of this operation caught the intrusion. Another early keylogger was a software keylogger written by Perry Kivolowitz in 1983. The user mode keylogger located and dumped character lists in a Unix kernel (similar to the keylogger we’ve created for this report). 

Overtime, and especially since the tech boom of the 1990s, keyloggers have broadened. Keylogger software is now even available for use on smartphones, such as the Apple iPhone and Android devices. However as technology has expanded more keylogger malware was developed, meaning attackers no longer had to install hardware keyloggers, enabling attackers to steal private data, such as credit card numbers, from unsuspecting victims in a remote location. The use of keyloggers started to target home users for fraud, as well as in different industries for phishing purposes. And while keyloggers do have some handy uses, which we will outline below, they have still mainly been used as a spyware tool by cybercriminals to steal personally identifiable information (PII), login credentials and sensitive enterprise data. Which is why understanding their origin and how they work are so important in regards to cybersecurity.

There are two types of keyloggers, hardware or software based. 
A hardware-based keylogger is a small device that serves as a connector between the keyboard and the computer. The device is designed to resemble an ordinary keyboard PS/2 connector, part of the computer cabling or a USB adaptor, making it relatively easy for someone who wants to monitor a user's behavior to hide the device.
A keylogging software program does not require physical access to the user's computer for installation. It can be purposefully downloaded by someone who wants to monitor activity on a particular computer, or it can be malware downloaded unwittingly and executed as part of a rootkit or remote administration Trojan (RAT). The rootkit can launch and operate stealthily to evade manual detection or antivirus scans.

How a keylogger works depends on its type. Hardware and software keyloggers work differently due to their medium.Most workstation keyboards plug into the back of the computer, keeping the connections out of the user's line of sight. 
A hardware keylogger may also come in the form of a module that is installed inside the keyboard itself. When the user types on the keyboard, the keylogger collects each keystroke and saves it as text in its own hard drive, which may have a memory capacity up to several gigabytes. The person who installed the keylogger must later return and physically remove the device to access the gathered information. There are also wireless keylogger sniffers that can intercept and decrypt data packets transferred between a wireless keyboard and its receiver.
A common software keylogger typically consists of two files that get installed in the same directory: a dynamic link library (DLL) file that does the recording and an executable file that installs the DLL file and triggers it. The keylogger program records each keystroke the user types and periodically uploads the information over the internet to whomever installed the program. Hackers can design keylogging software to use keyboard application program interfaces (APIs) to another application, malicious script injection or memory injection.

There are two main types of software keyloggers: user mode keyloggers and kernel mode keyloggers.
A user mode keylogger uses a Windows API to intercept keyboard and mouse movements. These keyloggers require the attacker to actively monitor each keypress. 
A kernel mode keylogger is a more powerful and complex software keylogging method. It works with higher privileges and can be harder to locate in a system. Kernel mode keyloggers use filter drivers that can intercept keystrokes. They can also modify the internal Windows system through the kernel.
Some keylogging programs may also include functionality to record user data besides keystrokes, such as capturing anything that has been copied to the clipboard and taking screenshots of the user's screen or a single application.

## What are some ethical keylogger uses?
While keyloggers have been associated with stealing sensitive information, they can also have ethical uses. However, it's important to use them responsibly and respect privacy. Here are some examples of ethical uses for keyloggers:

Parents can use keyloggers to monitor their children's online activity, ensuring they are safe and not engaging in dangerous behavior. Kido Protect Keylogger is an example of a software parents can use, allowing them to track search patterns, URLs, and social media accounts. Keyloggers can help prevent cyberbullying and protect children from online predators.

Employers can also use keyloggers to monitor their employees' computer activity and ensure they are not engaging in unauthorized activities or accessing sensitive information. This can also help monitor employee productivity. Keyloggers are commonly used in data entry jobs to monitor productivity. However, companies must be transparent and have policies in place regarding employee monitoring.

Law enforcement agencies can use keyloggers to track online activity of suspects and provide crucial evidence in criminal cases. However, using keyloggers for law enforcement purposes requires obtaining proper legal rights, such as a court order or warrant. The FBI used a keylogger in the case of Nicole Scarfo Jr., a Cosa Nostra mobster, to obtain evidence. A federal judge ruled the evidence was admissible in court.

Keyloggers can be used for personal use, such as keeping track of one's computer activity. They can help with time management, productivity tracking, and debugging software. Keyloggers can also be used for research purposes, analyzing user behavior and identifying areas for improvement in software or websites. They can also be used for educational purposes, teaching touch typing or providing feedback to students.

Keyloggers can be used as assistive technology for people with disabilities who have difficulty using a keyboard or mouse. Keyloggers can help these individuals access the technology they need to succeed. However, it's important to obtain proper permissions before using a keylogger. Using it without permission can be illegal and result in legal consequences.

## What are some unethical keylogger uses? & How do I remove one?
A keylogger is like a coin with two sides. It can be used for ethical purposes but at the same time, it can also be used for unethical purposes. 

For example, keyloggers can be used by script kiddies to steal login credentials to twitter, facebook and youtube accounts for pranking purposes. And by organized crime groups, stealing credit card, banking information and as well as identity theft, information like social security number, names and addresses. It’s also used by state-sponsored actors conducting espionage, gathering intelligence and spying between countries.

One of the most common keylogger attacks today is done through phishing emails, designed to trick the recipient into revealing sensitive information by getting them to click a link or download their attachments. Another way is malicious websites, so in the unfortunate event where the victim actually clicks the link from the phishing email, it'll probably take you to a website where the malware is downloaded automatically, or a website that looks identical to a legit website and asks for your login information while a keylogger is in place to log all input. Another way is Social engineering, malicious actors will purposely place usb drives in places likely to be found by unsuspecting victims like parking lots, coffee shops, lobbies and airports. And these usb can contain all sorts of malware including keyloggers.

We must be conscious of our cyber hygiene. When opening a link or downloading an attachment from emails, it’s a good practice to double check if the sender is from a legitimate source and that the link is consistent with the domain being sent from. For websites check the URL, make sure that it is spelled correctly and matches the website you intend to visit, check the website's certificates and if it uses secured encryption. Keep your system updated, and install keystroke encryption.

In the case that a keylogger has already been installed, running an anti-malware scan is one of the easiest and most straightforward methods to detect and remove the malware.
It’s also best practice to uninstall suspicious programs and always clear temporary files.
If you have a known malware free back-up, rolling back your system can also remove malware. And In the worst case scenario where you cannot remove the malware, resetting your system can be used as the last resort, ensuring that your system is malware-free.


References & Resources
1. Gillis, A. S. (2021, October 1). DEFINITION: Keylogger (keystroke logger or system monitor). TechTarget. Retrieved February 20, 2023, from https://www.techtarget.com/searchsecurity/definition/keylogger
2. Crowdstrike (2023, February 2). KEYLOGGERS: How they work and how to detect them. Retrieved February 21, 2023, from https://www.crowdstrike.com/cybersecurity-101/attack-types/keylogger/
3. (n.d.). Should You Use Keyloggers On Employee Computers. Currentware. Retrieved February 24, 2023, from https://www.currentware.com/blog/should-you-use-keyloggers-on-employee-computers/# alternative
4. Blue, V. (2017, June 28). Keyloggers: Beware this hidden threat. PC World. Retrieved February 24, 2023, from https://www.pcworld.com/article/406909/keyloggers-what-you-need-to-know-about-this-hi dden-threat.html
5. Chidi, G. A. (n.d.). Federal Judge Allows Key-board Stroke Capture. CNN. Retrieved February 24, 2023, from http://www.cnn.com/2002/TECH/internet/01/07/fbi.surveillance.idg/index.html
6. (n.d.). ChatGPT. https://chat.openai.com/chat

