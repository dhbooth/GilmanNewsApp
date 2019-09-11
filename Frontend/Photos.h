//
//  Photos.h
//  The Gilman News 5.0
//
//  Created by Davis Booth on 8/25/16.
//  Copyright © 2016 Davis Booth. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <MessageUI/MessageUI.h>

@interface Photos : UIViewController<UITextFieldDelegate, MFMailComposeViewControllerDelegate>
{
    IBOutlet UILabel *label;
    IBOutlet UITextField *email;
    IBOutlet UILabel *label2;
}
    
    
- (IBAction)touch:(id)sender;

- (IBAction)button:(id)sender;


@end
