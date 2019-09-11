//
//  Articles.h
//  The Gilman News 5.0
//
//  Created by Davis Booth on 8/25/16.
//  Copyright © 2016 Davis Booth. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <MessageUI/MessageUI.h>

@interface Articles : UIViewController<UITextViewDelegate, UITextFieldDelegate, MFMailComposeViewControllerDelegate>
{
    IBOutlet UITextField *email;
    IBOutlet UITextView *article;
    
}
- (IBAction)button:(id)sender;
- (IBAction)touch:(id)sender;

@end
