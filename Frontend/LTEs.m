//
//  LTEs.m
//  The Gilman News 5.0
//
//  Created by Davis Booth on 8/25/16.
//  Copyright © 2016 Davis Booth. All rights reserved.
//

#import "LTEs.h"

@interface LTEs ()

@end

@implementation LTEs

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

- (IBAction)button:(id)sender {
    MFMailComposeViewController *mailController = [[MFMailComposeViewController alloc] init];
    mailController.mailComposeDelegate = self;
    
    [mailController setToRecipients:@[@"thegilmannews@gmail.com"]];
    [mailController setSubject: [email.text stringByAppendingString: @" Letter to the Editor Submission"]];
    [mailController setMessageBody:textViews.text isHTML:NO];
    [self presentViewController:mailController animated:YES completion:nil];
}

- (IBAction)touch:(id)sender {
    [self.view endEditing:YES];
}

- (void)mailComposeController:(MFMailComposeViewController *)controller didFinishWithResult:(MFMailComposeResult)result error:(NSError *)error
{
    [self dismissViewControllerAnimated:YES completion:nil];
    
}

- (BOOL) textViewShouldEndEditing:(UITextView *)textView
{
    [textViews resignFirstResponder];
    return YES;
}

- (BOOL) textFieldShouldReturn:(UITextField *)textField
{
    [email resignFirstResponder];
    return YES;
}

@end
